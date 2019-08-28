function cMoney(dollars) {
    return (dollars).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,')
  }
   function popPage(){
      d3.json(`${location.pathname}/json`).then(function(data){
          var edition = data.edition
          var config = data.config
          var term = data.maint_years
          d3.select("#edition-header").html(`${edition}<br>${term} Year M&S Extension`);
          d3.select("#quote-info").html(`Quote prepared by ${data.bsc_name} on ${data.quote_date}<br>for <b><i>${data.cx_name}</b></i> (customer ID: ${data.cx_sapid})<br>Account Executive: ${data.rep_name}`);
          var officialuse = d3.select("#official-use")
            officialuse.append("tr").html(`<td>Purchase Code</td><td>${data.pcode}</td>`)
            officialuse.append("tr").html(`<td>Registration ID</td><td>${data.rid}</td>`)
            officialuse.append("tr").html(`<td></td><td></td>`)
            officialuse.append("tr").html(`<td></td><td></td>`)

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