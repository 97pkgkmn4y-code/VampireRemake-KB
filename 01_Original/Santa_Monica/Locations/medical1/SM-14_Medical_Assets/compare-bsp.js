// Compare selected authored entities with the installed UP BSP entity lump.
const fs=require('fs'),path=require('path');
const mapName=process.argv[2]||'sm_medical_1';
if(!/^sm_[a-z0-9_]+$/.test(mapName))throw new Error('Invalid map name');
const dataPath=process.argv[3]?path.resolve(process.argv[3]):path.join(__dirname,'vmf-extract.json');
const d=require(dataPath);
const p=path.resolve(__dirname,'../../../../../../Reference/Vampire - The Masquerade Bloodlines/Unofficial_Patch/maps/'+mapName+'.bsp');
const b=fs.readFileSync(p),off=b.readInt32LE(8),len=b.readInt32LE(12),src=b.toString('latin1',off,off+len);
const entities=[...src.matchAll(/\{([^{}]*)\}/g)].map(m=>Object.fromEntries([...m[1].matchAll(/"([^"]+)"\s+"([^"]*)"/g)].map(k=>[k[1],k[2]])));
const names=process.argv[4]?process.argv[4].split(','):['clinic_guard','guard_warning','guard_warning-wesp','guard_sees_player','player_on_floor_two','restricted_section','nurse_talk_trigger','camera_cs','camera_prescriptions','Lily','Vandal','Phil','Heather','MedicalTeleport1','MedicalTeleport2','garou_blood'];
for(const name of names){
 const a=d.entities.filter(e=>e.targetname===name),c=entities.filter(e=>e.targetname===name);
 const same=a.length===c.length&&a.every(e=>c.some(v=>v.classname===e.classname&&(!e.origin||v.origin===e.origin)));
 console.log(name,a.length,c.length,same?'match':'DIFF');
}
console.log('BSP',b.toString('ascii',0,4),b.readInt32LE(4),'entities',entities.length);
