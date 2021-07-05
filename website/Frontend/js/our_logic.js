
console.log("dddddddddddddddzzzzzzzz")







/* 
fetch('http://127.0.0.1:8000/tasks').
then(res => res.json()).
then(data => {console.log(data)
  data.forEach((e,i) => {
    
var aTag = document.createElement("a")
var div = document.createElement("div")
if (i==0){
  aTag.setAttribute('class',"list-group-item list-group-item-action active");
  div.setAttribute('class',"tab-pane fade active show");
}else{
  aTag.setAttribute('class',"list-group-item list-group-item-action");
  div.setAttribute('class',"tab-pane fade");
}

aTag.setAttribute('id',e.id_+"-list");
aTag.setAttribute('data-toggle',"tab");
aTag.setAttribute('role',"tab");
aTag.setAttribute('href',"#"+e.id_);
aTag.setAttribute('aria-controls',e.id_);
aTag.innerText = e.title;
var element = document.getElementById("list-tab");
element.appendChild(aTag);

div.setAttribute('role',"tabpanel");
div.setAttribute('id',e.id_);
div.setAttribute('aria-labelledby',e.id_+"-list");

var p = document.createElement("p")
console.log(e.text)
p.innerText = e.text
div.appendChild(p)
var element = document.getElementById("nav-tabContent");
element.appendChild(div);

 });
    } ) */

//handle form data



function uuidv4() {
return 'axxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
return v.toString(16);
});
}

