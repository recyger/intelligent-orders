/**
 * Created by Vladislav on 05.04.2015.
 */
var users = app.controller("transportationStatusController", ['$scope', '$http',
    function ($scope, $http) {
        var modal = $('#modal'),
            _set = function (data) {
                var empty = {};
                $.each($scope.data || {}, function(key){
                    empty[key] = null;
                });
                angular.copy(data || empty, $scope.data);
            },
            _get = function () {
                $http.post('/transportation_status/list')
                    .success(function (data) {
                        $scope.status = data['data'];
                        $('[data-toggle="tooltip"]').tooltip();
                    });
            };
        $scope.data = {};
        $scope.status = [];
        $scope.onCreate = function (event) {
            event.preventDefault();
            _set();
            modal.modal('show');
        };
        $scope.onEdit = function (event) {
            event.preventDefault();
            _set($scope.status[event.currentTarget.attributes['data-target'].value]);
            modal.modal('show');
        };
        $scope.submitData = function () {
            $http.post('/transportation_status/save', {'status': $scope.data})
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