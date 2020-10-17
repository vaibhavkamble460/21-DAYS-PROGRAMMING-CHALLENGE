#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;


int main() {
    int t, n;
    cin >> t;
    while(t--) {
        cin >> n;
        int arr[n];
        set<int> s;
        vector<int> result;
        for(int i = 0; i < n; i++) { 
            cin >> arr[i];
            if(s.find(arr[i]) == s.end())
                result.push_back(arr[i]);
            s.insert(arr[i]);
        }
        if(result.size() <= 1) {
            cout << -1 << endl;
            continue;
        }
        sort(result.begin(), result.end(), greater<int>());
        cout << result[1] << endl;
    }
    return 0;
}
