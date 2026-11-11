const fs=require('fs'),path=require('path'),d=require('./vmf-extract.json');
const X=x=>100+x+136,Y=y=>625-(y+128),esc=s=>String(s).replaceAll('&','&amp;').replaceAll('<','&lt;');
const poly=(v,cls,tip)=>`<polygon class="${cls}" points="${v.map(p=>X(p[0])+','+Y(p[1])).join(' ')}"><title>${esc(tip)}</title></polygon>`;
let s=`<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="700" viewBox="0 0 1400 700"><rect width="1400" height="700" fill="#101820"/><style>text{font-family:Segoe UI,Arial,sans-serif;fill:#e7e7e3}.h{font-size:25px;font-weight:700}.sm{font-size:14px}.grid{stroke:#324750}.floor{fill:#355c68;stroke:#90b5bf;stroke-width:1;fill-opacity:.78}.wall{fill:#8c6e59;stroke:#c5a58c;stroke-width:1;fill-opacity:.8}.trigger{fill:#b876b9;stroke:#ddb7e0;stroke-width:2;fill-opacity:.3}.npc{fill:#8bdaa3;stroke:#101820;stroke-width:2}.event{fill:#f1b56b;stroke:#101820;stroke-width:2}.number{font-size:12px;fill:#101820;font-weight:bold}</style><text class="h" x="28" y="35">Santa Monica Diner — VMF coordinate plan</text><text class="sm" x="28" y="58">World X/Y · clipped brush polygons near Z=0–17 · wall section Z=40 · points are entity origins</text>`;
for(const x of [0,200,400,600,800])s+=`<line class="grid" x1="${X(x)}" x2="${X(x)}" y1="${Y(-128)}" y2="${Y(408)}"/><text class="sm" x="${X(x)+3}" y="${Y(-128)+19}">${x}</text>`;
for(const y of [-100,0,100,200,300,400])s+=`<line class="grid" x1="${X(-136)}" x2="${X(832)}" y1="${Y(y)}" y2="${Y(y)}"/><text class="sm" x="51" y="${Y(y)+5}">${y}</text>`;
for(const f of d.faces.filter(f=>[0,8,17].includes(f.z)&&f.area>2000))s+=poly(f.vertices,'floor',`solid ${f.solid}, side ${f.side}, Z=${f.z}, VMF L${f.line}`);
for(const c of d.sections.filter(c=>c.z===40&&['worldspawn','func_detail'].includes(c.parent)&&c.area<9000)){
 const xs=c.vertices.map(p=>p[0]),ys=c.vertices.map(p=>p[1]);if(Math.min(Math.max(...xs)-Math.min(...xs),Math.max(...ys)-Math.min(...ys))>48)continue;
 s+=poly(c.vertices,'wall',`solid ${c.solid}, section Z=40`);
}
for(const c of d.sections.filter(c=>c.z===40&&/trigger_/.test(c.parent||'')))s+=poly(c.vertices,'trigger',`${c.targetname}, solid ${c.solid}`);
const names=['diner1','Doris','basic_cook','plus_cook','diner_patron_male','diner_patron_female','Killer','assassin_s','assassin_e','assassin_w','assassin_n','SMphone','dindoora','trigger_attack','lilly_purse'];
s+=`<rect x="1082" y="74" width="290" height="590" rx="10" fill="#1c2a33" stroke="#4c6671"/><text class="h" x="1100" y="104">Entity anchors</text>`;
let i=0;for(const name of names){const e=d.entities.find(e=>e.targetname===name);if(!e?.origin)continue;const p=e.origin.split(' ').map(Number);i++;const cls=/^npc_/.test(e.classname)?'npc':'event';s+=`<circle class="${cls}" cx="${X(p[0])}" cy="${Y(p[1])}" r="8"><title>${name}, ${e.classname}, ID ${e.id}, (${e.origin}), VMF L${e.line}</title></circle><text class="number" x="${X(p[0])-4}" y="${Y(p[1])+4}">${i}</text><text class="sm" x="1100" y="${134+(i-1)*29}">${i}. ${name} · ${e.id}</text>`;}
s+=`<text class="sm" x="1100" y="605">Blue: brush top · Brown: wall section</text><text class="sm" x="1100" y="628">Green: NPC · Orange: entity point</text><text class="sm" x="28" y="680">Source: UP SDK sm_diner_1.vmf · Geometry is not a verified movement graph</text></svg>`;
fs.writeFileSync(path.join(__dirname,'SM-15_Diner_Plan.svg'),s);
