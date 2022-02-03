//Instructions(100 points):
//Please add comments to your program.
//Upload lab #3 to the appropriate drop box in Blackboard.
//Use the following naming convention: [Name]_lab3_[Problem #]
//Suppose you can buy a chocolate bar from the vending machine for $1 each. Inside every chocolate bar is a coupon. You can redeem seven coupons for one chocolate bar from the machine. You would like to know how many chocolate bars you can eat, including from those redeemed via coupon, if you have n dollars.
//
//For example, if you have 20 dollars then you can initially buy 20 chocolate bars. This gives you 20 coupons. You can redeem 14 coupons for twoadditional chocolate bars. These two additional chocolate bars give you two more coupons, so you now have a total of eight coupons. This gives you enough to redeem for one final chocolate bar. As a result you now have 23 chocolate bars and two leftover coupons.
//
//Write a program that inputs the number of dollars and outputs how many chocolate bars you can collect after spending all your money and redeeming as many coupons as possible. Also output the number of leftover coupons. The easiest way to solve thisproblem is to use a loop.
//
//Hint:You will need to use integer division and modulus for this program
//Output:
//
//Enter in the amount of money you have: 20
//You can buy 23 chocolate bars and have 2 leftover coupons.
//
//Enter in the amount of money you have: 50
//You can buy 58 chocolate bars and have 2 leftover coupons.
//
//Enter in the amount of money you have: 11
//You can buy 12 chocolate bars and have 5 leftover coupons.#include <iostream>

#include <iostream>

using namespace std;
int main()
{
    int dollarNum = 0;
    int barNum = 0;
    int couponNum = 0;

cin >> "Enter how many dollar you have: ";

    while (dollarNum >= 1)
    {
        barNum++;
        dollarNum++;
        couponNum++;
    };
    while (couponNum >=7)
    {
        barNum++;
        couponNum - 7;
    };
    
    cout << "You can buy " << barNum << " and have " << couponNum << " leftover coupons." << endl;
    system("Pause");
    return 0;
}