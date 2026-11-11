// Structural DLG row extraction; numeric links only, no inferred adjacency.
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../../../../../../Reference/Vampire - The Masquerade Bloodlines/Unofficial_Patch/dlg/santa monica');
const files=(process.argv[2]||'clinic_guard,nurse,malcolm,phil,lily,vandal').split(',');
if(files.some(f=>!/^\w+$/.test(f)))throw new Error('Invalid DLG name');
const outDir=process.argv[3]?path.resolve(process.argv[3]):__dirname;
if(!fs.existsSync(outDir))throw new Error('Output directory missing');
const csvName=process.argv[4]||'SM-14_Dialogue_Rows.csv';
if(!/^SM-\d+_Dialogue_Rows\.csv$/.test(csvName))throw new Error('Invalid output name');
const q=v=>'"'+String(v||'').replaceAll('"','""')+'"';
const rows=[];
for(const name of files){
 const lines=fs.readFileSync(path.join(root,name+'.dlg'),'utf8').split(/\r?\n/);
 for(let i=0;i<lines.length;i++){
  const parts=[...lines[i].matchAll(/\{([^{}]*)\}/g)].map(m=>m[1].trim());
  if(parts.length<7||!/^\d+$/.test(parts[0]))continue;
  rows.push({file:name,line:i+1,id:parts[0],text:parts[1],next:parts[3],field4:parts[4],field5:parts[5],field6:parts[6],fields:parts.length});
 }
}
const cols=['file','line','id','text','next','field4','field5','field6'];
fs.writeFileSync(path.join(outDir,csvName),cols.join(',')+'\n'+rows.map(r=>cols.map(k=>q(r[k])).join(',')).join('\n')+'\n');
for(const file of files){const a=rows.filter(r=>r.file===file);console.log(file,a.length,'starting',a.filter(r=>r.text.includes('Starting Condition')).map(r=>r.id+':'+r.field4+'→'+r.next).join('; '));}
