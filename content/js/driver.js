/**
 * Created by Vladislav on 05.04.2015.
 */
var users = app.controller("driverController", ['$scope', '$http',
    function ($scope, $http) {
        var modal = $('#modal'),
            _set = function (data) {
                var empty = {};
                $.each($scope.data || {}, function(key){
                    empty[key] = null;
                });
                angular.copy(data || empty, $scope.data);
                //$("#address").select2()
                //.on("change", function() {
                //        $scope.data.address = $scope.data.address;
                //});
            },
            _get = function () {
                $http.post('/driver_status/list')
                    .success(function (data) {
                        $scope.status = data['data'];
                    });
                $http.post('/driver/list')
                    .success(function (data) {
                        $scope.driver = data['data'];
                        $('[data-toggle="tooltip"]').tooltip();
                    });
            };
        $scope.data = {};
        $scope.status = [];
        $scope.driver = [];
        $scope.onCreate = function (event) {
            event.preventDefault();
            _set();
            modal.modal('show');
        };
        $scope.onEdit = function (event) {
            event.preventDefault();
            _set($scope.driver[event.currentTarget.attributes['data-target'].value]);
            modal.modal('show');
        };
        $scope.submitData = function () {
            $http.post('/driver/save', {'status': $scope.data})
                .success(function () {
                    _get();
                    modal.modal('hide');
                })
                .error(function (data, status) {
                    console.log(data, status);
                });
        };
        $scope.onDelete = function (event) {
            var url = event.currentTarget.href;
            event.preventDefault();
            bootbox.confirm("Вы уверены?", function (result) {
                if (result) {
                    $http.post(url)
                        .success(function () {
                            _get();
                        })
                        .error(function (data, status) {
                            console.log(data, status);
                        });
                }
            });
        };
        _get();
        _set();
    }]);