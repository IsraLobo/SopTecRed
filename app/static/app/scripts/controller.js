var app = angular.module("MyAccesoAng", []);
var ruta = '/consulta/';

app.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

app.controller("ControllerHTTP", function ($scope, $http) {
    $scope.newConsulta = {};

    $scope.realizarConsult = function () {
        var msisdn = $scope.newConsulta.msisdn;
        var serie = $scope.newConsulta.serie;
        var sim = $scope.newConsulta.sim;

        if (msisdn == null || msisdn == undefined || msisdn == "null" || msisdn == "undefined") { msisdn = "" }
        else if (msisdn.length != 10 && msisdn.length != 0) {
            $scope.datosVacios = 'ERROR: El MSISDN debe de ser a 10 digitos';
            $scope.visDtos = false;
            $scope.datosBD = '';
            return;
        }
        if (serie == null || serie == undefined || serie == "null" || serie == "undefined") { serie = "" }
        else if (serie.length != 13 && serie.length != 0) {
            $scope.datosVacios = 'ERROR: La SERIE debe de ser a 13 digitos';
            $scope.visDtos = false;
            $scope.datosBD = '';
            return;
        }
        if (sim == null || sim == undefined || sim == "null" || sim == "undefined") { sim = "" }
        else if (sim.length != 20 && sim.length != 0) {
            $scope.datosVacios = 'ERROR: El ICC debe de ser a 20 digitos';
            $scope.visDtos = false;
            $scope.datosBD = '';
            return;
        }

        $http.post(ruta,
            {
                "msisdn": msisdn,
                "serie": serie,
                "sim": sim
            }).then(function (response) {
                if (response.data == 0) {
                    $scope.datosVacios = 'ERROR: Favor de ingresar un dato correcto.';
                    $scope.visDtos = false;
                    $scope.datosBD = '';
                } else {
                    $scope.datosVacios = '';
                    $scope.visDtos = true;
                    $scope.datosBD = response.data;
                }
            }, function (err) {
                console.log(err)
            });
    }

});