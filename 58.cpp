#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        auto new_end = remove(nums.begin(), nums.end(), val);
        nums.erase(new_end, nums.end());
        return nums.size();
    }
};

int main() {
    Solution s;
    vector<int> nums = {3, 2, 2, 3};
    int val = 2;
    cout << s.removeElement(nums, val) << endl;

    for (int num : nums) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
