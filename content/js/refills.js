/**
 * Created by Vladislav on 05.04.2015.
 */
var users = app.controller("refillsController", ['$scope', '$http',
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
                $http.post('/driver/list')
                    .success(function (data) {
                        $scope.driver = data['data'];
                    });
                $http.post('/truck/list')
                    .success(function (data) {
                        $scope.truck = data['data'];
                    });
                $http.post('/refills/list')
                    .success(function (data) {
                        $scope.refills = data['data'];
                        $('[data-toggle="tooltip"]').tooltip();
                    });
            };
        $scope.data = {};
        $scope.driver = [];
        $scope.truck = [];
        $scope.refills = [];
        $scope.opened = false;

        $scope.open = function ($event) {
            $event.preventDefault();
            $event.stopPropagation();

            $scope.opened = true;
        };

        $scope.dateOptions = {
            'formatYear': 'yy',
            'startingDay': 1,
            'show-button-bar': false,
            'current-text': 'Сегодня'
        };

        $scope.onCreate = function (event) {
            event.preventDefault();
            _set();
            modal.modal('show');
        };
        $scope.onEdit = function (event) {
            event.preventDefault();
            _set($scope.refills[event.currentTarget.attributes['data-target'].value]);
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