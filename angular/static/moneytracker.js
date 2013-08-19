var moneytracker = angular.module("moneytracker", ['ngResource']);

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
				templateUrl: 'transactions/'
			})
			.otherwise({
				redirectTo: '/'
			});
	}
]);

moneytracker.controller('debtController', function($scope) {


});

moneytracker.controller('transactionController', function($scope, $resource) {
	$scope.transList = $resource('/api/v1/transaction').get(function() {
		$scope.numberOfRecords = $scope.transList.meta.total_count;
		$scope.pageSize = $scope.transList.meta.limit;
		$scope.offset = $scope.transList.meta.offset;
		$scope.numberOfPages = Math.ceil($scope.numberOfRecords/$scope.pageSize);
	});

	$scope.GoToPage = function(page) {
		$scope.transList = $resource('/api/v1/transaction/?limit=20&offset=' + $scope.pageSize * page)
			.get(function() {
				$scope.numberOfRecords = $scope.transList.meta.total_count;
				$scope.pageSize = $scope.transList.meta.limit;
				$scope.offset = $scope.transList.meta.offset;
				$scope.numberOfPages = Math.ceil($scope.numberOfRecords/$scope.pageSize);
			}
		);
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