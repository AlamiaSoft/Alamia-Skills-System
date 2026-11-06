#!/usr/bin/env node
"use strict";
const fs=require("node:fs"),path=require("node:path");
const ROOT=path.resolve(__dirname,"..");
function usage(){console.log(`Alamia Skills Installer
Usage: npx alamia-skills-install --seo|--content|--marketing|--video|--research|--business|--engineering|--all
Options: --list --target <project-dir> --force --dry-run --help
Installs into <project-dir>/.agents/skills/. Existing skills are preserved unless --force is used.`);}
function parse(argv){
 const o={collection:null,target:process.cwd(),force:false,dryRun:false,list:false,help:false};
 for(let i=0;i<argv.length;i++){const a=argv[i];
  if(a==="--help"||a==="-h")o.help=true;else if(a==="--list")o.list=true;else if(a==="--force")o.force=true;else if(a==="--dry-run")o.dryRun=true;
  else if(a==="--target"){if(!argv[i+1])throw Error("--target requires a directory");o.target=path.resolve(argv[++i]);}
  else if(a.startsWith("--")){if(o.collection)throw Error("Choose one collection at a time, or use --all");o.collection=a.slice(2).toLowerCase();}
  else throw Error("Unexpected argument: "+a);
 }return o;
}
function main(argv=process.argv.slice(2)){
 try{
  const o=parse(argv);if(o.help)return usage();
  const mf=JSON.parse(fs.readFileSync(path.join(ROOT,"catalog/collections.json"),"utf8"));
  if(mf.schemaVersion!==1||!mf.collections)throw Error("Invalid or unsupported collections manifest");
  const names=Object.keys(mf.collections).sort();
  if(o.list){for(const n of names)console.log(n.padEnd(14)+mf.collections[n].description+" ("+mf.collections[n].skills.length+" skills)");return;}
  if(!o.collection){usage();process.exitCode=1;return;}
  const selected=o.collection==="all"?names:[o.collection],unknown=selected.filter(n=>!mf.collections[n]);
  if(unknown.length)throw Error("Unknown collection: "+unknown.join(", ")+". Use --list.");
  const destRoot=path.join(o.target,".agents","skills");let installed=0,skipped=0;
  for(const name of selected){const col=mf.collections[name];console.log("\n"+col.title+" — "+col.description);
   for(const e of col.skills){
    if(!e||typeof e.id!=="string"||typeof e.source!=="string")throw Error("Invalid skill entry in "+name);
    const src=path.resolve(ROOT,e.source);if(!src.startsWith(ROOT+path.sep))throw Error("Unsafe source path: "+e.source);
    const skill=path.join(src,"SKILL.md"),meta=path.join(src,"skill.json");
    if(!fs.existsSync(skill)||!fs.statSync(skill).isFile()||!fs.existsSync(meta))throw Error("Incomplete skill package: "+e.source);
    const m=JSON.parse(fs.readFileSync(meta,"utf8"));for(const k of ["id","name","description","domain","version"])if(typeof m[k]!=="string"||!m[k].trim())throw Error("Missing "+k+" in "+meta);
    if(m.id!==e.id)throw Error("Skill ID mismatch: "+e.id+" != "+m.id);
    const dest=path.join(destRoot,e.id);
    if(o.dryRun){console.log("  [DRY RUN] "+e.id);installed++;continue;}
    if(fs.existsSync(dest)&&!o.force){console.log("  [SKIP] "+e.id+" already exists");skipped++;continue;}
    fs.mkdirSync(destRoot,{recursive:true});if(o.force&&fs.existsSync(dest))fs.rmSync(dest,{recursive:true,force:true});fs.cpSync(src,dest,{recursive:true,force:o.force,dereference:false});console.log("  [OK] "+e.id);installed++;
   }
  }
  console.log(o.dryRun?"\nDry run: "+installed+" skill(s) would be installed.":"\nComplete: "+installed+" installed, "+skipped+" preserved. Destination: "+destRoot);
 }catch(e){console.error("Error: "+e.message);process.exitCode=1;}
}
if(require.main===module)main();
module.exports={main,parse};
