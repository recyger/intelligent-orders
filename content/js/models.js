/**
 * Created by Vladislav on 05.04.2015.
 */
var users = app.controller("moddelController", ['$scope', '$http',
    function ($scope, $http) {
        var modal = $('#formModel'),
            conf = $('#formAlett'),
            set_model = function (data) {
                $scope.model = $.extend({
                    'id': null,
                    'name': '',
                    'passwd': '',
                    'role': null
                }, data || {});
            },
            get_users = function () {
                $http.post('/model/list')
                    .success(function (data) {
                        $scope.models = data['models'];
                        $('[data-toggle="tooltip"]').tooltip();
                    });
            };
        $scope.models = [];
        $scope.onGenPass = function (event) {
            event.preventDefault();
            $scope.model.passwd = generatePassword(6, false, /\d/);
        };
        $scope.onEdit = function (event) {
            event.preventDefault();
            set_model($scope.models[event.currentTarget.attributes['data-target'].value]);
            modal.modal('show');
        };
        $scope.submitData = function () {
            $http.post('/model/save', {"model": $scope.model})
                .success(function () {
                    get_users();
                    modal.modal('hide');
                })
                .error(function(data, status){
                    console.log(data, status);
                });
        };
        $scope.onDelete = function(event){
            event.preventDefault();
            $http.post(event.currentTarget.href)
                .success(function(){
                    get_users();
                })
                .error(function(data, status){
                    console.log(data, status);
                });
        };
        modal.on('hide.bs.modal', function () {
            set_model();
        });
        get_users();
        set_model();
    }]);