class Solution {
public:
    int s;
    int addDigits(int num) {
        while(num > 9)
        {
           s = 0;
            while(num)
            {
                s += num%10;
                num = num/10;
            }
            num = s;
        }
        return num;
    }
};
