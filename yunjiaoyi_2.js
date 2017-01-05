localStorage.setItem("s1", "Smith");
localStorage.setItem("s2", "Smith");
localStorage.setItem("s3", "Smith");


var prefix = "http://api.pushingbox.com/pushingbox?devid=";

var st1_max = "vA6D38F47E4AED82";
var st1_min = "vBE2600910E47896";
var st2_max = "v006DC4E1FC89B30";
var st2_min = "vCBB561C15F61CC7";
var st3_max = "vDE1C741AF25DCC2";
var st3_min = "v123B48C25160238";

var maxAPI = [st1_max, st2_max, st3_max];
var minAPI = [st1_min, st2_min, st3_min];

//css color scheme
var red = 'color:red';
var blue = 'color:blue';
var green = 'color:green';


function pushNoti(theUrl){
	var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, true ); // false for synchronous request
    xmlHttp.send();
};



var spanTags = document.getElementsByTagName('span');

var Stock = function(tagPos, maxVal, minVal){
	
	this.tagPos = tagPos
	this._now = spanTags[tagPos].innerHTML
	this._max = maxVal
	this._min = minVal

};


// stock id, max, min
var st_1 = new Stock(5, 200, 100);
var st_2 = new Stock(7, 200, 100);
var st_3 = new Stock(9, 200, 100);

var stocks = [st_1, st_2, st_3];

var main = function(){
	for (i = 0; i < stocks.length; i++){
		st_run = stocks[i]
		//console.log('now: ' + st_run._now + ' ' + st_run._min + ' ' + st_run._max)
		console.log('%s: %c%s, %c%s, %c%s',i, blue, st_run._now, red, st_run._max, green, st_run._min)

		if(st_run._now != spanTags[st_run.tagPos].innerHTML){
			// reassign value
			st_run._now = spanTags[st_run.tagPos].innerHTML

			// check max
			if (st_run._now >= st_run._max){
				//push alert action
				st_run._max = st_run._now
				var url = prefix + maxAPI[i]
				pushNoti(url)
				//console.log('max_value stock: ' + i + ', max_now' + st_run._max)
				console.log('Stock %s %cReach max stock! new max vlaue: %s', i, red, st_run._max)
			}
			// check min
			if (st_run._now <= st_run._min){
				// push alert action
				st_run._min = st_run._now
				var url = prefix + minAPI[i]
				pushNoti(url)
				//console.log('min_value stock: ' + i + ', min_now' + st_run._min)
				console.log('Stock %s %cReach min stock! new min vlaue: %s', i, green, st_run._min)
			}	
			
		}
	}
}
main()