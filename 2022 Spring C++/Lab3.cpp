#include <iostream>

using namespace std;

int main() {
    // Additional variables for program flexibilty
    int dollarNum = 0;
    int barNum = 0;
    int couponNum = 0;
    int dollarCost = 1;
    int couponCost = 7;

    cout << "Enter how many dollars you have: ";
    cin >> dollarNum;

    // Fast calculations
    barNum = dollarNum / dollarCost + dollarNum / couponCost;
    couponNum = dollarNum % couponCost;

    // Alternative calculations with while loops
//    while (dollarNum >= dollarCost)
//    {
//        barNum++;
//        dollarNum -= dollarCost;
//        couponNum++;
//    }
//    while (couponNum >= couponCost)
//    {
//        barNum++;
//        couponNum -= couponCost;
//    }

    // Diplay results
    cout << "You can buy " << barNum << " chocolate bars and have " << couponNum << " leftover coupons." << endl;
    system("Pause");
    return 0;
}