const $=s=>document.querySelector(s);let catalogue=null,searchIndex={};
function node(tag,cls,text){const n=document.createElement(tag);if(cls)n.className=cls;if(text!==undefined)n.textContent=text;return n}
function normalize(value){return String(value||"").normalize("NFKD").replace(/[\\u0300-\\u036f]/g,"").toLowerCase().replace(/[^a-z0-9]+/g," ").trim()}
const SEARCH_ALIASES={
 website:["website","websites","web application","web applications","web app","web apps","frontend","front end","web pwa"],
 websites:["website","websites","web application","web applications","web app","web apps","frontend","front end","web pwa"],
 site:["site","sites","website","web application","web app","frontend"],
 sites:["site","sites","website","web application","web app","frontend"]
};
function matchesQuery(skill,query){
 const haystack=normalize([skill.name,skill.description,skill.id,skill.domain,...(skill.tags||[]),searchIndex[skill.id]||""].join(" "));
 return normalize(query).split(" ").filter(Boolean).every(term=>(SEARCH_ALIASES[term]||[term]).some(alias=>haystack.includes(normalize(alias))));
}
function render(){
 const q=$("#search").value.trim(),filter=$("#collection-filter").value;
 const found=catalogue.skills.filter(s=>(!filter||s.collection===filter)&&matchesQuery(s,q));
 $("#skill-count").textContent=catalogue.skills.length;$("#collection-count").textContent=catalogue.collections.length;
 $("#result-count").textContent=found.length+" of "+catalogue.skills.length+" skills";
 const grid=$("#skill-grid");grid.replaceChildren();$("#empty").hidden=found.length!==0;
 for(const s of found){const a=node("a","skill-card");a.href=s.skill_page||("skill.html?id="+encodeURIComponent(s.id));const top=node("div","card-top");top.append(node("span","pill",s.collection),node("span","version","v"+s.version));a.append(top,node("h3","",s.name),node("p","",s.description));const bottom=node("div","card-bottom");bottom.append(node("span","",s.domain),node("b","","View skill ↗"));a.append(bottom);grid.append(a)}
 const cg=$("#collection-grid");cg.replaceChildren();for(const c of catalogue.collections){const card=node("article","collection-card");card.append(node("span","count",c.skills.length+" SKILLS"),node("h3","",c.title),node("p","",c.description));const pre=node("pre","",c.install);card.append(pre);cg.append(card)}
}
async function start(){try{const [catalogueResponse,indexResponse]=await Promise.all([fetch("data/catalog.json"),fetch("data/search-index.json")]);if(!catalogueResponse.ok||!indexResponse.ok)throw Error("Catalogue or search index request failed");[catalogue,searchIndex]=await Promise.all([catalogueResponse.json(),indexResponse.json()]);const select=$("#collection-filter");for(const c of catalogue.collections){const o=node("option","",c.title);o.value=c.id;select.append(o)}$("#search").addEventListener("input",render);select.addEventListener("change",render);render()}catch(e){$("#result-count").textContent="Catalogue unavailable. Please try again later.";console.error(e)}}
start();
