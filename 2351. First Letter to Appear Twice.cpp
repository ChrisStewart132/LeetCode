/*
Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

    A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
    s will contain at least one letter that appears twice.

*/
class Solution {
public:
    char repeatedCharacter(string s) {
        std::unordered_set<char> cache(26);
        for(const char& c: s){
            if(cache.find(c) != cache.end()){
                return c;
            }
            cache.insert(c);
        }
        return 0;
    }
};