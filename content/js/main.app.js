/**
 * Created by Vladislav on 31.03.2015.
 */
var app = angular.module('mainModule', ['ui.bootstrap'])
        .config(function ($sceProvider) {
            $sceProvider.enabled(false);
        });