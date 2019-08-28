function cMoney(dollars) {
  return (dollars).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')
}
function popPage(){
    d3.json(`${location.pathname}/json`).then(function(data){
        var edition = data.edition
        var dist_nodes = data.nodes.distribute_nodes
        var proc_nodes = data.nodes.process_nodes
        var input_nodes = data.nodes.input_nodes
        var config = data.config
        
        input_nodes.forEach((node) => {
          d3.select("#input-node-list")
          .append("li")
          .text(node)
        });
        proc_nodes.forEach((node) => {
          d3.select("#process-node-list")
          .append("li")
          .text(node)
        });
        dist_nodes.forEach((node) => {
          d3.select("#distribute-node-list")
          .append("li")
          .text(node)
        });
        d3.select("#edition-header").text(`Dispatcher Phoenix: ${edition}`);
        d3.select("#quote-info").html(`Quote prepared by ${data.bsc_name} on ${data.quote_date}<br>for ${data.cx_name} (customer ID: ${data.cx_sapid})<br>Account Executive: ${data.rep_name}`);

        var selector = d3.select("#pricing-body");
        config.forEach((item) => {
            selector.append("tr")
                    .html(`<td>${item.sap_num}</td><td>${item.item_desc}</td><td>$${cMoney(item.price)}</td><td>${item.qty}</td><td>$${cMoney(item.ext_price)}</td>`)
        })
        
        selector.append("tr").html(`<td></td><td></td><td></td><td><b>TOTAL</b></td><td><b>$${cMoney(data.total_price)}</b></td>`)
    })
}

function init() {
    popPage()
}

init()