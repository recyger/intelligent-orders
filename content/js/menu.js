/**
 * Created by Vladislav on 05.04.2015.
 */

var menu = app.controller("menuController", ['$scope', '$http',
    function ($scope, $http) {
        var _t = 0,
            init = function () {
                clean_data();
                $scope.body = '/content/work.html';
                get_menu();
            },
            clean_data = function () {
                $scope.menus = [];
                $scope.url = '';
                $scope.body = '/content/welcome.html';
            },
            get_menu = function () {
                $http.post("/menu")
                    .success(function (data) {
                        $scope.menus = data['data'];
                    });
            };
        $scope.onMenuAction = function ($event) {
            $event.preventDefault();
            $scope.url = $event.currentTarget.attributes.href.value;
            $scope.body = '/content/' + $event.currentTarget.attributes.href.value + '.html?_t='+_t++;
        };
        init();
    }]);