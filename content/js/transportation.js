/**
 * Created by Vladislav on 05.04.2015.
 */
var users = app.controller("transportationController", ['$scope', '$http',
    function ($scope, $http) {
        var modal = $('#modal'),
            _set = function (data) {
                var empty = {};
                $.each($scope.data || {}, function (key) {
                    empty[key] = null;
                });
                angular.copy(data || empty, $scope.data);
                //$("#address").select2()
                //.on("change", function() {
                //        $scope.data.address = $scope.data.address;
                //});
            },
            _get = function () {
                $scope.get_address(1);
                $scope.get_driver(1);
                $scope.get_order(1);
                $scope.get_truck(1);
                $http.post('/transportation/list')
                    .success(function (data) {
                        $scope.transportation = data['data'];
                        $('[data-toggle="tooltip"]').tooltip();
                    });
            };

        $scope.data = {};
        $scope.transportation = [];
        $scope.tachometer = {};

        $scope.calc = function ($event) {
            if ($event) {
                $event.preventDefault();
                $event.stopPropagation();
            }
            if ($scope.tachometer.end && $scope.tachometer.start) {
                $('#mileage').val(parseFloat($scope.tachometer.end) - parseFloat($scope.tachometer.start));
            }
        };
        $scope.onCreate = function (event) {
            event.preventDefault();
            _set();
            modal.modal('show');
        };
        $scope.onEdit = function (event) {
            event.preventDefault();
            _set($scope.transportation[event.currentTarget.attributes['data-target'].value]);
            modal.modal('show');
        };
        $scope.submitData = function () {
            $http.post('/transportation/save', {'status': $scope.data})
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