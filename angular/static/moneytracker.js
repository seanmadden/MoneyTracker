var moneytracker = angular.module("moneytracker", ['ngResource', 'ngRoute', 'moneyServices', 'ngCookies']);

moneytracker.config(['$routeProvider',
	function($routeProvider){

//		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
//		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

		$routeProvider
			.when('/',
			{
				controller: 'debtController',
				templateUrl: 'debt/'
			})
			.when ('/transactions',
			{
				controller: 'transactionController',
				templateUrl: 'transactions/',
				resolve: {
					transactions: function(transactionResource) {
						return transactionResource.getResource().get().$promise;
					}
				}
			})
			.when('/add',
			{
				controller: 'addController',
				templateUrl: 'add/',
				resolve: {
					userList: function(userResource) {
						return userResource.getResource().get().$promise;
					},
					transactionTypes: function(transactionTypeResource) {
						return transactionTypeResource.getResource().get().$promise;
					}
				}
			})
			.otherwise({
				redirectTo: '/'
			});
	}
]);

moneytracker.config(['$httpProvider',
	function($httpProvider) {
		$httpProvider.defaults.headers.common['X-CSRFToken'] = $('input[name="csrfmiddlewaretoken"]').val();
	}
]);

moneytracker.controller('debtController', function($scope) {


});

moneytracker.controller('addController',
	function addController($scope, $resource, userList, transactionTypes, $http) {

		$scope.trans = {};
		$scope.isDisabled = false;

		$scope.userList = userList.objects;
		//default to the first option
		$scope.trans.user = $scope.userList[0];

		$scope.transactionTypes = transactionTypes.objects;
		$scope.trans.transaction_type = $scope.transactionTypes[0];

		$scope.addTransaction = function() {

			$scope.isDisabled = true;
			$http.post('/api/v1/transaction/', $scope.trans);


		}

});

moneytracker.controller('transactionController',
	function transactionController($scope, $resource, transactions) {

	$scope.transList = transactions;
	parseResource();

	$scope.NextPage = function() {
		$scope.transList = $resource($scope.nextLink).get(parseResource);
	};

	$scope.PreviousPage = function() {
		$scope.transList = $resource($scope.previousLink).get(parseResource);
	};

	$scope.GoToPage = function(page) {
		$scope.transList = $resource('/api/v1/transaction/?limit=20&offset=' + $scope.pageSize * page)
			.get(parseResource);
	};

	function parseResource() {
		$scope.numberOfRecords = $scope.transList.meta.total_count;
		$scope.pageSize = $scope.transList.meta.limit;
		$scope.offset = $scope.transList.meta.offset;
		$scope.numberOfPages = Math.ceil($scope.numberOfRecords/$scope.pageSize);
		$scope.nextLink = $scope.transList.meta.next;
		$scope.previousLink = $scope.transList.meta.previous;
	}

});

moneytracker.filter('range', function() {
	return function(input, total) {
		total = parseInt(total);
		for (var i=0; i<total; i++)
			input.push(i);
		return input;
	};
});


angular.module('moneyServices', ['ngResource'])
	.factory('userResource', function($resource) {
		var userResource = $resource('/api/v1/user');

		userResource.prototype.getResource = function() {
			return userResource;
		};

		return new userResource;
	})
	.factory('transactionResource', function($resource) {
		var transResource = $resource('/api/v1/transaction');

		transResource.prototype.getResource = function() {
			return transResource;
		};

		return new transResource;
	})
	.factory('transactionTypeResource', function($resource) {
		var transactionTypeResource = $resource('/api/v1/transaction_type');

		transactionTypeResource.prototype.getResource = function() {
			return transactionTypeResource;
		};

		return new transactionTypeResource;
	});
