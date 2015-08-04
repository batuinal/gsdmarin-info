$(document).ready(function() {
    $('#example').dataTable( {
	
	serverSide: false,
	data: [
		{
			"name": "Tiger Nixon",
			"position": "System Architect",
			"salary": "$3,120"
		},
		{
			"name": "Garrett Winters",
			"position": "Director",
			"salary": "$5,300"
		}
	],
	columns: [
        { data: 'name' },
        { data: 'position' },
        { data: 'salary' }
    ]
	
	} );
	
	editor = new $.fn.dataTable.Editor( {
		serverSide: false,
		table: "#example",
		fields: [
			{ label: 'name', name: 'name' },
			{ label: 'position',  name: 'position'  },
			{ label: 'salary',  name: 'salary'  }
			]
	} );
	
	$('#example').on( 'click', 'tbody td:not(:first-child)', function (e) {
        editor.inline( this );
    } );
	
	
} );