#include <iostream>
#include <iomanip>
using namespace std;
class Bank
{
public:
  string name;
  string accType;
  int bal;
  int accNo;
  int with;
  int dep;
  void deposit()
  {
    cin >> name >> accNo >> accType >> bal;
    cin >> dep;
    bal = bal + dep;
    cout << bal << endl;
  }
  void withdraw()
  {
    cin >> with;
    if (with <= bal)
    {
      bal -= with;
      cout<< "NAME=" << name << "\nACCNO=" << accNo << "\nTYPE=" << accType << "\nBALANCE=" << bal << endl;
    }
    else
    {
      cout << "Insufficient balance\n" << "NAME="<<name<<" ACCNO="<<accNo<<"\nTYPE="<<accType<<"\nBALANCE="<<bal<<endl;
    }
  }
};
int main()
{
  Bank obj;
  obj.deposit();
  obj.withdraw();
  return 0;
}