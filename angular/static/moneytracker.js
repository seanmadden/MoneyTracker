var moneytracker = angular.module("moneytracker", ['ngResource', 'moneyServices']);

moneytracker.config(['$routeProvider',
	function($routeProvider){
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
					loadData: function(transactionResource) {
						return transactionResource.getTransList().promise;
					}
				}
			})
			.when('/add',
			{
				controller: 'addController',
				templateUrl: 'add/'
			})
			.otherwise({
				redirectTo: '/'
			});
	}
]);

moneytracker.controller('debtController', function($scope) {


});

moneytracker.controller('addController', function($scope) {

});

var transactionController = moneytracker.controller('transactionController', function($scope, $resource) {

//	init();
	$scope.transResource = $resource('/api/v1/transaction');
//	$scope.transactions = transactions;

	function init() {
		$scope.transList = $resource('/api/v1/transaction').get(parseResource);
	}

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



//moneytracker.controller('transactionController', transactionController);

moneytracker.filter('range', function() {
	return function(input, total) {
		total = parseInt(total);
		for (var i=0; i<total; i++)
			input.push(i);
		return input;
	};
});


angular.module('moneyServices', ['ngResource'])
	.factory('transactionResource', function($resource) {
		var transResource = $resource('/api/v1/transaction');

		transResource.prototype.getTransList = function() {
			return transResource.get();
		};

		return new transResource;
	});