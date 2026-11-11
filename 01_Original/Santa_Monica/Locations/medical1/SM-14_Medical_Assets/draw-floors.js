// Render polygons clipped against all planes of each VMF brush.
const fs=require('fs'),path=require('path'),d=require('./vmf-extract.json');
const levels=[
 {slug:'Basement',floor:-336,cut:-296,door:-286,names:['Lily','Vandal','Phil','morgue_trunk','Morguedr','vandaldr','employee_entrance']},
 {slug:'Ground',floor:0,cut:40,door:54,names:['Nurse','Heather','Malcolm','medical1','medical2','stairwaydoor','meddrfrntr','officef','morphinedr']},
 {slug:'Upper',floor:192,cut:232,door:246,names:['clinic_guard','cis','smmc','garou_blood','topfloordr','controlledsubstancesdr','prescripsdr','securitydr','camera_cs','camera_prescriptions']}
];
const esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;');
const X=x=>76+(x-633)*.62,Y=y=>970-(y+36)*.62;
const poly=(pts,cls,title)=>`<polygon class="${cls}" points="${pts.map(p=>X(p[0])+','+Y(p[1])).join(' ')}"><title>${esc(title)}</title></polygon>`;
for(const l of levels){
 let s=`<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="1040" viewBox="0 0 1100 1040"><rect width="1100" height="1040" fill="#101820"/><style>text{font-family:Segoe UI,Arial,sans-serif;fill:#e6e7e4}.h{font-size:25px;font-weight:bold}.sub{font-size:13px}.grid{stroke:#334853;stroke-width:1}.floor{fill:#365b68;stroke:#92b5bf;stroke-width:1;fill-opacity:.8}.wall{fill:#896d5b;stroke:#c6a98d;stroke-width:1;fill-opacity:.75}.trigger{fill:#b36cba;stroke:#dcb1e2;stroke-width:2;fill-opacity:.25}.door{fill:#ffbc68;stroke:#121921;stroke-width:2}.npc{fill:#8bd69d;stroke:#121921;stroke-width:2}.item{fill:#f0e277;stroke:#121921;stroke-width:2}.other{fill:#83bfff;stroke:#121921;stroke-width:2}.number{font-size:11px;fill:#101820;font-weight:bold}.legend{font-size:14px}</style><text class="h" x="28" y="35">Santa Monica Medical Clinic — ${l.slug}</text><text class="sub" x="28" y="58">VMF world coordinates · clipped brush polygons, floor Z=${l.floor}, wall section Z=${l.cut}</text>`;
 for(const x of [800,1000,1200,1400,1600])s+=`<line class="grid" x1="${X(x)}" x2="${X(x)}" y1="${Y(-36)}" y2="${Y(1356)}"/><text class="sub" x="${X(x)+3}" y="${Y(-36)+18}">${x}</text>`;
 for(const y of [0,400,800,1200])s+=`<line class="grid" x1="${X(633)}" x2="${X(1620)}" y1="${Y(y)}" y2="${Y(y)}"/><text class="sub" x="36" y="${Y(y)+4}">${y}</text>`;
 for(const f of d.faces.filter(f=>Math.abs(f.z-l.floor)<.1&&f.vertices.every(p=>p[0]>=630&&p[0]<=1625&&p[1]>=-40&&p[1]<=1360)))s+=poly(f.vertices,'floor',`floor solid ${f.solid}, side ${f.side}, VMF L${f.line}, Z=${f.z}`);
 for(const c of d.sections.filter(c=>c.z===l.cut&&['worldspawn','func_detail','func_brush'].includes(c.parent)&&c.area<10000)){
  const xs=c.vertices.map(p=>p[0]),ys=c.vertices.map(p=>p[1]);if(Math.min(Math.max(...xs)-Math.min(...xs),Math.max(...ys)-Math.min(...ys))>48)continue;
  s+=poly(c.vertices,'wall',`solid ${c.solid}, section Z=${l.cut}, parent=${c.parent}`);
 }
 for(const c of d.sections.filter(c=>c.z===l.cut&&/trigger_/.test(c.parent||'')&&/restricted_section|nurse_talk_trigger|player_on_floor_two/.test(c.targetname||'')))s+=poly(c.vertices,'trigger',`${c.targetname}, solid ${c.solid}`);
 s+=`<rect x="745" y="75" width="326" height="885" rx="12" fill="#1b2932" stroke="#506975"/><text class="h" x="765" y="109">Entity anchors</text>`;
 let idx=0;
 for(const name of l.names){
  const matches=d.entities.filter(e=>e.targetname?.toLowerCase()===name.toLowerCase()&&e.origin&&Math.abs(Number(e.origin.split(' ')[2])-l.door)<100);
  for(const e of matches.slice(0,2)){
   idx++;const p=e.origin.split(' ').map(Number),type=/^npc_/.test(e.classname)?'npc':/^item_/.test(e.classname)?'item':/door|dr$/.test(e.classname+' '+name)?'door':'other';
   s+=`<circle class="${type}" cx="${X(p[0])}" cy="${Y(p[1])}" r="8"><title>${esc(name)} ID ${e.id}, (${e.origin}), VMF L${e.line}</title></circle><text class="number" x="${X(p[0])-3}" y="${Y(p[1])+4}">${idx}</text>`;
   s+=`<text class="legend" x="765" y="${139+(idx-1)*32}">${idx}. ${esc(name)} <tspan fill="#9fb2b9">ID ${e.id}</tspan></text>`;
  }
 }
 s+=`<text class="legend" x="765" y="660">Legend</text><rect class="floor" x="765" y="681" width="19" height="14"/><text class="sub" x="793" y="693">horizontal brush face</text><rect class="wall" x="765" y="707" width="19" height="14"/><text class="sub" x="793" y="719">thin solid at section height</text><rect class="trigger" x="765" y="733" width="19" height="14"/><text class="sub" x="793" y="745">restricted/talk trigger</text><circle class="door" cx="775" cy="772" r="7"/><text class="sub" x="793" y="777">door origin</text><circle class="npc" cx="775" cy="799" r="7"/><text class="sub" x="793" y="804">NPC origin</text><text class="sub" x="765" y="848">Adjacency does not prove a route.</text><text class="sub" x="765" y="870">Model geometry is not included.</text><text class="sub" x="28" y="1020">Source: SDK UP sm_medical_1.vmf · Hover SVG elements for IDs · Brush polygons clipped by all side planes</text></svg>`;
 fs.writeFileSync(path.join(__dirname,`SM-14_Medical_${l.slug}.svg`),s);
}
