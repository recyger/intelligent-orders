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

        $scope.get_address = function (status) {
            if (!status) {
                status = null;
            }
            $http.post('/address/list', {'status': status})
                .success(function (data) {
                    $scope.address = data['data'];
                });
        };

        $scope.get_order = function (status) {
            if (!status) {
                status = null;
            }
            $http.post('/order/list', {'status': status})
                .success(function (data) {
                    $scope.order = data['data'];
                });
        };

        $scope.get_driver = function (status) {
            if (!status) {
                status = null;
            }
            $http.post('/driver/list', {'status': status})
                .success(function (data) {
                    $scope.driver = data['data'];
                });
        };

        $scope.get_truck = function (status) {
            if (!status) {
                status = null;
            }
            $http.post('/truck/list', {'status': status})
                .success(function (data) {
                    $scope.truck = data['data'];
                });
        };

        $scope.address = [];
        $scope.order = [];
        $scope.driver = [];
        $scope.truck = [];
        $scope.onMenuAction = function ($event) {
            $event.preventDefault();
            $scope.url = $event.currentTarget.attributes.href.value;
            $scope.body = '/content/' + $event.currentTarget.attributes.href.value + '.html?_t=' + _t++;
        };
        init();
    }]);