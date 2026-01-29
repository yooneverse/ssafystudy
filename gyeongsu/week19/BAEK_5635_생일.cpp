#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <string>
using namespace std;

int years(int d, int m , int y){
    return y * 10000 + m * 100 + d;
}


int main() {

    int n;
    cin >> n;
    
    string name;
    int d, m, y;
    int oldest, youngest;
    string old_name, young_name;
    
    cin >> name;
    cin >> d >> m >> y;
    old_name = young_name = name;
    oldest = youngest = years(d,m,y);
    
    for(int i=1; i < n; i++){
        int year;
        cin >> name;
        cin >> d >> m >> y;
        year = years(d, m, y);
        
        if (year > oldest){
            oldest = year;
            old_name = name;
        }
        
        if (year < youngest) {
            youngest = year;
            young_name = name;
        }
        
    }
    
    cout << old_name << endl << young_name;
    
    return 0;
}