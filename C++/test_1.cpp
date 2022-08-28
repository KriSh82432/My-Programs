#include <iostream>
#include <cstring>
using namespace std;
int main()
{
    char s[10001];
    int test;
    int i = 0;
    int total = 0;
    cin >> test;
    while (i < test)
    {
        
        cin >> s;
        cout << s << endl;
        for (int i = 0; i < strlen(s); ++i)
        {
            int val = isdigit(s);
            if (val)
            {
                cout << "True" << endl;
            }
            else
            {
                cout << "False" << endl;
            }
        }
        ++i;
    }
    return 0;
}