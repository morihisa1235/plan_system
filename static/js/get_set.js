        window.onload = function onLoad() {
          var param = GetQueryString();

          var target = document.getElementById("param_search_out");
          if (param == null || param["search"] == undefined) {
            target.innerHTML = "パラメーターはありません。";
          } else {
            target.innerHTML = param["search"];
          }

          var target = document.getElementById("param_mode_out");
          if (param == null || param["mode"] == undefined) {
            target.innerHTML = "パラメーターはありません。";
          }
          else {
            target.innerHTML = param["mode"];
          }
        }

        function GetQueryString() {
            if (1 < document.location.search.length) {
                var query = document.location.search.substring(1);
                var parameters = query.split('&');

                var result = new Object();
                for (var i = 0; i < parameters.length; i++) {
                    var element = parameters[i].split('=');

                    var paramName = decodeURIComponent(element[0]);
                    var paramValue = decodeURIComponent(element[1]);

                    result[paramName] = decodeURIComponent(paramValue);
                }
                return result;
            }
            return null;
        }

function clickBtn3(){
	document.getElementById("param_search_out").setAttribute("value","青");
}