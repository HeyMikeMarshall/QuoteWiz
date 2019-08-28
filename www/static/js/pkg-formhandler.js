function buildPrimaryTable(edition) {
  d3.select("#input-node-list").html("");
  d3.select("#process-node-list").html("");
  d3.select("#distribute-node-list").html("");
  d3.select("#primary-license").html("");
  d3.selectAll(".optchk")
    .property("checked", false)
    .property("disabled", false);
  d3.json(`/dispatcher/phoenix/editions/${edition}`).then(function(data){
    var inc_opts = data.inc_opts
    inc_opts.forEach((opt) => {
      d3.select(`#${opt[1]}-chk`)
      .property("checked", "true")
      .property("disabled", "true")
    });
    })
  };
function qtyChkChanged(state, name) {
  var selector = d3.select(`#${name}-opts`)
  var checked = state
  if (checked === true) {selector.attr("hidden",null)}
  if (checked === false) {selector.attr("hidden","true")}
}
function getDate() {
  var today = new Date();
  var dd = today.getDate();
  var mm = today.getMonth()+1;
  var yyyy = today.getFullYear();
  if(dd<10) {dd = '0'+dd} 
  if(mm<10) {mm = '0'+mm} 
  today = yyyy + '-' + mm + '-' + dd;
  d3.select("#datepicker").attr("value",today);
}
window.onload = function() {
  getDate();
};

function init() {
  var selector = d3.select("#selEdition");
  d3.json("/dispatcher/phoenix/editions").then((editions) => {
    selector
      .append("option")
      .text("--Select Base Edition--")
      .property("value", "default")
    
    editions.forEach((edition) => {
      selector
        .append("option")
        .text(edition)
        .property("value", edition);
    });

  });
}
function optionChanged(edition) {
  buildPrimaryTable(edition);
}
init();
