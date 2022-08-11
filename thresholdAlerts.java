public static void main(String[] args) {
	int[] numCalls = {2,2,2,2,5,5,5,8};
	int alertThreshold = 4, precedingMinutes = 3;
	System.out.println(getNumOfAlerts(numCalls, alertThreshold, precedingMinutes));
}

private static int getNumOfAlerts(int[] numCalls, int alertThreshold, int precedingMinutes) {
	int[] preSum = new int[numCalls.length + 1];
	int res = 0;
	for(int i=1;i<preSum.length;i++) {
		preSum[i] = numCalls[i-1] + preSum[i-1];
	}
	for(int i=precedingMinutes;i<=numCalls.length;i++) {
		if((preSum[i] - preSum[i-precedingMinutes])/precedingMinutes > alertThreshold)
			res++;
	}
	return res;
}