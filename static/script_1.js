google.charts.load('current', { 'packages': ['table'] });
google.charts.setOnLoadCallback(drawTable);

function drawTable() {

  var result = JSON.parse("{{data|escapejs}}");
  var dict = result;
  console.log(typeof (dict));
  console.log(dict);

  var data = new google.visualization.DataTable();

  data.addColumn('string', 'Username');
  data.addColumn('number', 'Rating');
  data.addColumn('number', 'Highest Rating');
  data.addColumn('number', 'Global Rank');
  data.addColumn('number', 'Country Rank');

  for (let i = 0; i < dict.length; i++) {
    var arr = [];
    for (var key in dict[i]) {
      if (dict[i].hasOwnProperty(key)) {
        arr.push(dict[i][key]);
      }
    }
    data.addRows([arr]);
  }

  var table = new google.visualization.Table(document.getElementById('table_div'));
   var options = {
      sort: 'Rating',
      // sortColumn: 1,
      sortAscending: true 
  };
  table.draw(data,options);
}