//Author: Junlin Wang
//https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=391
#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    getline(cin,s);
    int t = stoi(s);
    int count = 0;
        vector<string> names;
        vector<pair<string,int>> to_sort;
        vector<string> deps;
        vector<string> home_phone;
        vector<string> work_phone;
        vector<string> campus_box;
        vector<string> address;
    for (int i = 0 ; i<t;++i)
    {
        string dep;
        getline(cin,dep);
        string line;
        while (getline(cin,line))
        {
            if (line == "")
            {
                /* cout<<i<<endl; */
                break;
            }
            /* cout<<line<<endl; */
            stringstream ss(line);
            //whlie (ss.good())
            string title;
            getline(ss,title,',');
            string first;
            getline(ss,first,',');
            string last;
            getline(ss,last,',');
            deps.push_back(dep);
            string name = title + " " + first + " "  + last;
            /* cout<<name<<endl; */
            names.push_back(name);
            string substr;
            getline(ss,substr,',');
            address.push_back(substr);
            getline(ss,substr,',');
            home_phone.push_back(substr);
            getline(ss,substr,',');
            work_phone.push_back(substr);
            getline(ss,substr,'\n');
            /* cout<<substr<<endl; */
            campus_box.push_back(substr);
            to_sort.push_back(make_pair(last,count));
            count++;
        }

    }

        sort(to_sort.begin(),to_sort.end());
        for (auto x: to_sort)
        {
            printf("----------------------------------------\n");
            int ind = x.second;
            cout<<names[ind]<<endl;
            cout<<address[ind]<<endl;
            cout<<"Department: "<<deps[ind]<<endl;
            cout<<"Home Phone: "<<home_phone[ind]<<endl;
            cout<<"Work Phone: "<<work_phone[ind]<<endl;
            cout<<"Campus Box: "<<campus_box[ind]<<endl;
        }
}
