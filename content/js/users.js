/**
 * Created by Vladislav on 05.04.2015.
 */
var users = app.controller("userController", ['$scope', '$http',
    function ($scope, $http) {
        var modal = $('#formUser'),
            set_user = function (data) {
                $scope.user = angular.copy( data || {} );
            },
            get_users = function () {
                $http.post('/user/list')
                    .success(function (data) {
                        $scope.users = data['users'];
                        $scope.roles = data['roles'];
                        $('[data-toggle="tooltip"]').tooltip();
                    });
            };
        $scope.users = [];
        $scope.roles = [];
        $scope.onGenPass = function (event) {
            event.preventDefault();
            $scope.user.passwd = generatePassword(6, false, /\d/);
        };
        $scope.onEdit = function (event) {
            event.preventDefault();
            set_user($scope.users[event.currentTarget.attributes['data-target'].value]);
            modal.modal('show');
        };
        $scope.submitData = function () {
            $http.post('/user/save', {'user': $scope.user})
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
            set_user();
        });
        get_users();
        set_user();
    }]);