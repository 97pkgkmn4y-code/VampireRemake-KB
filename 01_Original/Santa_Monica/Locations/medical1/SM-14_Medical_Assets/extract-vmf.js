// Reproducible, read-only extraction of the UP Plus VMF's nested blocks.
const fs = require('fs');
const path = require('path');
const mapName=process.argv[2]||'sm_medical_1';
if(!/^sm_[a-z0-9_]+$/.test(mapName))throw new Error('Invalid map name');
const outDir=process.argv[3]?path.resolve(process.argv[3]):__dirname;
if(!fs.existsSync(outDir))throw new Error('Output directory missing: '+outDir);
const sectionZ=process.argv[4]?process.argv[4].split(',').map(Number):[-296,40,232];
if(sectionZ.some(v=>!Number.isFinite(v)))throw new Error('Invalid section heights');
const src = path.resolve(__dirname, '../../../../../../Reference/Vampire - The Masquerade Bloodlines/SDKContent/MapSrc/up sources/'+mapName+'.vmf');
const lines = fs.readFileSync(src, 'utf8').split(/\r?\n/);
const roots = [], stack = [];
let pending = null;
for (let i = 0; i < lines.length; i++) {
  const s = lines[i].trim();
  if (!s || s.startsWith('//')) continue;
  if (s === '{') {
    const n = { type: pending, line: i + 1, props: {}, entries: [], children: [], parent:stack.at(-1)||null };
    (stack.at(-1)?.children || roots).push(n); stack.push(n); pending = null;
  } else if (s === '}') stack.pop();
  else if (s.startsWith('"')) {
    const m = s.match(/^"([^"]+)"\s+"(.*)"$/);
    if (m && stack.length) { stack.at(-1).props[m[1]] = m[2]; stack.at(-1).entries.push({key:m[1],value:m[2],line:i+1}); }
  } else pending = s;
}
const all = n => [n, ...n.children.flatMap(all)];
const nodes = roots.flatMap(all);
const entities = nodes.filter(n => n.type === 'entity');
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const dot=(a,b)=>a[0]*b[0]+a[1]*b[1]+a[2]*b[2];
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const faces=[], sections=[];
for (const solid of nodes.filter(n=>n.type==='solid')) {
  const sides=solid.children.filter(c=>c.type==='side').map(side=>{
    const points=[...(side.props.plane||'').matchAll(/\((-?[\d.]+) (-?[\d.]+) (-?[\d.]+)\)/g)].map(m=>m.slice(1).map(Number));
    if(points.length!==3)return null;
    let normal=cross(sub(points[1],points[0]),sub(points[2],points[0]));
    const len=Math.hypot(...normal);if(len<1e-8)return null;
    normal=normal.map(v=>v/len);
    return {side,points,normal,d:dot(normal,points[0])};
  }).filter(Boolean);
  if(sides.length<4)continue;
  const center=[0,1,2].map(k=>sides.reduce((a,s)=>a+s.points.reduce((v,p)=>v+p[k],0),0)/(sides.length*3));
  for(const s of sides)if(dot(s.normal,center)>s.d+1e-5){s.normal=s.normal.map(v=>-v);s.d=-s.d;}
  for(const z of sectionZ){
    const vertices=[];
    for(let j=0;j<sides.length;j++)for(let k=j+1;k<sides.length;k++){
      const b=sides[j],c=sides[k],a={normal:[0,0,1],d:z};
      const bc=cross(b.normal,c.normal),ca=cross(c.normal,a.normal),ab=cross(a.normal,b.normal);
      const det=dot(a.normal,bc);if(Math.abs(det)<1e-7)continue;
      const p=[0,1,2].map(t=>(a.d*bc[t]+b.d*ca[t]+c.d*ab[t])/det);
      if(sides.some(s=>dot(s.normal,p)>s.d+.08))continue;
      if(!vertices.some(q=>Math.hypot(...sub(p,q))<.08))vertices.push(p);
    }
    if(vertices.length<3)continue;
    const centroid=[0,1].map(t=>vertices.reduce((a,p)=>a+p[t],0)/vertices.length);
    vertices.sort((a,b)=>Math.atan2(a[1]-centroid[1],a[0]-centroid[0])-Math.atan2(b[1]-centroid[1],b[0]-centroid[0]));
    const area=Math.abs(vertices.reduce((a,p,t)=>a+p[0]*vertices[(t+1)%vertices.length][1]-vertices[(t+1)%vertices.length][0]*p[1],0)/2);
    if(area<100)continue;
    sections.push({solid:solid.props.id,z,parent:solid.parent?.props.classname||solid.parent?.type,targetname:solid.parent?.props.targetname||'',vertices:vertices.map(p=>p.map(v=>Math.round(v*100)/100)),area:Math.round(area)});
  }
  for(let i=0;i<sides.length;i++){
    const face=sides[i]; if(face.normal[2]<.97)continue;
    const vertices=[];
    for(let j=0;j<sides.length;j++)for(let k=j+1;k<sides.length;k++){
      if(j===i||k===i)continue;
      const a=face,b=sides[j],c=sides[k];
      const bc=cross(b.normal,c.normal),ca=cross(c.normal,a.normal),ab=cross(a.normal,b.normal);
      const det=dot(a.normal,bc);if(Math.abs(det)<1e-7)continue;
      const p=[0,1,2].map(t=>(a.d*bc[t]+b.d*ca[t]+c.d*ab[t])/det);
      if(sides.some(s=>dot(s.normal,p)>s.d+.08))continue;
      if(!vertices.some(q=>Math.hypot(...sub(p,q))<.08))vertices.push(p);
    }
    if(vertices.length<3)continue;
    const centroid=[0,1].map(t=>vertices.reduce((a,p)=>a+p[t],0)/vertices.length);
    vertices.sort((a,b)=>Math.atan2(a[1]-centroid[1],a[0]-centroid[0])-Math.atan2(b[1]-centroid[1],b[0]-centroid[0]));
    const area=Math.abs(vertices.reduce((a,p,t)=>a+p[0]*vertices[(t+1)%vertices.length][1]-vertices[(t+1)%vertices.length][0]*p[1],0)/2);
    if(area<150)continue;
    faces.push({solid:solid.props.id,side:face.side.props.id,line:face.side.line,material:face.side.props.material,entity:solid.__entity||null,z:Math.round(vertices.reduce((a,p)=>a+p[2],0)/vertices.length*100)/100,vertices:vertices.map(p=>p.map(v=>Math.round(v*100)/100)),area:Math.round(area)});
  }
}
const eout = entities.map(n => ({line:n.line, ...n.props, outputs:n.children.filter(c=>c.type==='connections').flatMap(c=>c.entries.map(e=>({event:e.key,value:e.value,line:e.line})))}));
fs.writeFileSync(path.join(outDir,'vmf-extract.json'), JSON.stringify({source:src, world:roots.find(n=>n.type==='world')?.props, entities:eout, faces, sections},null,2));
console.log(JSON.stringify({lines:lines.length,entities:entities.length,faces:faces.length,sections:sections.length,classes:[...new Set(entities.map(e=>e.props.classname))].length}));
