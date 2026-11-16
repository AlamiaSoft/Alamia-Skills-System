/* Safe, dependency-free Markdown renderer for the Alamia Skills portal.
   HTML is treated as text; elements are created through DOM APIs only. */
(function(){
 const inlinePattern=/(!?\[[^\]]*\]\([^)]*\)|\*\*[^*]+\*\*|__[^_]+__|~~[^~]+~~|\*[^*\n]+\*|_[^_\n]+_|\x60+[^\x60]+\x60+)/g;
 function safeUrl(raw){try{const u=new URL(raw,location.href);return ["http:","https:","mailto:"].includes(u.protocol)?u.href:null}catch{return null}}
 function inline(text,parent){
  const pattern=new RegExp(inlinePattern.source,"g");let last=0,m;
  while((m=pattern.exec(text))!==null){
   parent.append(document.createTextNode(text.slice(last,m.index)));
   const token=m[0];let node=null;
   if(token.startsWith("![")){const x=token.match(/^!\[([^\]]*)\]\(([^)]+)\)$/);if(x){const url=safeUrl(x[2]);if(url){node=document.createElement("img");node.alt=x[1];node.src=url;node.loading="lazy";node.referrerPolicy="no-referrer"}}}
   else if(token.startsWith("[")){const x=token.match(/^\[([^\]]+)\]\(([^)]+)\)$/);if(x){const url=safeUrl(x[2]);if(url){node=document.createElement("a");node.href=url;node.rel="noopener noreferrer";node.textContent=x[1];if(url.startsWith("http"))node.target="_blank"}}}
   else if(token.startsWith("`")){node=document.createElement("code");node.textContent=token.replace(/^`+|`+$/g,"")}
   else if(token.startsWith("**")||token.startsWith("__")){node=document.createElement("strong");inline(token.slice(2,-2),node)}
   else if(token.startsWith("~~")){node=document.createElement("del");inline(token.slice(2,-2),node)}
   else{node=document.createElement("em");inline(token.slice(1,-1),node)}
   parent.append(node||document.createTextNode(token));last=m.index+token.length;
  }
  parent.append(document.createTextNode(text.slice(last)));
 }
 function render(source,target){
  const lines=source.replace(/^\uFEFF/,"").replace(/\r\n?/g,"\n").split("\n");
  if(lines[0]==="---"){const end=lines.indexOf("---",1);if(end>0)lines.splice(0,end+1)}
  target.replaceChildren();let i=0;
  const isSpecial=l=>/^\s*(```|#{1,6}\s|>|[-*+]\s|\d+[.)]\s|\|.*\|\s*$|([-*_])\2\2+\s*$)/.test(l);
  function blocks(parent,stopQuote=false){
   while(i<lines.length){
    let line=lines[i];if(!line.trim()){i++;continue}
    if(stopQuote&&!/^\s*>/.test(line))break;
    const fence=line.match(/^\s*(```+|~~~+)(.*)$/);
    if(fence){const marker=fence[1][0],size=fence[1].length,lang=fence[2].trim();i++;const code=[];while(i<lines.length&&!new RegExp("^\\s*"+marker+"{"+size+",}").test(lines[i]))code.push(lines[i++]);if(i<lines.length)i++;
     const wrap=document.createElement("section");wrap.className="md-code-block";const bar=document.createElement("div");bar.className="md-code-toolbar";const label=document.createElement("span");label.textContent=lang||"CODE";const copy=document.createElement("button");copy.type="button";copy.className="md-copy";copy.textContent="Copy";copy.addEventListener("click",async()=>{try{await navigator.clipboard.writeText(code.join("\n"));copy.textContent="Copied";setTimeout(()=>copy.textContent="Copy",1400)}catch{copy.textContent="Copy unavailable"}});bar.append(label,copy);const pre=document.createElement("pre"),c=document.createElement("code");if(lang)c.dataset.language=lang;c.textContent=code.join("\n");pre.append(c);wrap.append(bar,pre);parent.append(wrap);continue}
    const heading=line.match(/^\s*(#{1,6})\s+(.+?)\s*#*\s*$/);if(heading){const h=document.createElement("h"+heading[1].length);inline(heading[2],h);parent.append(h);i++;continue}
    if(i+1<lines.length&&/^\s*(=+|-+)\s*$/.test(lines[i+1])){const h=document.createElement(lines[i+1].trim()[0]==="="?"h1":"h2");inline(line.trim(),h);parent.append(h);i+=2;continue}
    if(/^\s*([-*_])\s*\1\s*\1(?:\s*\1)*\s*$/.test(line)){parent.append(document.createElement("hr"));i++;continue}
    if(/^\s*>/.test(line)){const q=document.createElement("blockquote");while(i<lines.length&&/^\s*>/.test(lines[i]))lines[i]=lines[i++].replace(/^\s*>\s?/,"");blocks(q,true);parent.append(q);continue}
    if(/^\s*([-*+]\s+|\d+[.)]\s+)/.test(line)){const ordered=/^\s*\d/.test(line),list=document.createElement(ordered?"ol":"ul");while(i<lines.length&&/^\s*([-*+]\s+|\d+[.)]\s+)/.test(lines[i])){const item=lines[i++].replace(/^\s*(?:[-*+]\s+|\d+[.)]\s+)/,"");const li=document.createElement("li");inline(item,li);list.append(li)}parent.append(list);continue}
    if(line.includes("|")&&i+1<lines.length&&/^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$/.test(lines[i+1])){const rows=[line];i+=2;while(i<lines.length&&lines[i].includes("|")&&lines[i].trim())rows.push(lines[i++]);const table=document.createElement("table"),thead=document.createElement("thead"),tbody=document.createElement("tbody");const cells=s=>s.trim().replace(/^\||\|$/g,"").split("|").map(x=>x.trim());cells(rows[0]).forEach(v=>{const th=document.createElement("th");inline(v,th);thead.append(th)});for(const row of rows.slice(1)){const tr=document.createElement("tr");cells(row).forEach(v=>{const td=document.createElement("td");inline(v,td);tr.append(td)});tbody.append(tr)}table.append(thead,tbody);parent.append(table);continue}
    const p=document.createElement("p"),parts=[line.trim()];i++;while(i<lines.length&&lines[i].trim()&&!isSpecial(lines[i])&&!/^\s*>/.test(lines[i]))parts.push(lines[i++].trim());inline(parts.join(" "),p);parent.append(p);
   }
  }
  blocks(target);
 }
 window.AlamiaMarkdown={render};
})();