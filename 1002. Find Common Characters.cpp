/*
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
*/

class Solution {
public:
    std::vector<std::string> commonChars(std::vector<std::string>& words) {
        std::unordered_map<char, int> commonMap;
        for (const char& c : words[0]) {
            commonMap[c]++;
        }

        // Iterate through the rest of the words and find the common characters
        for (int i = 1; i < words.size(); i++) {
            std::unordered_map<char, int> tempMap;
            for (const char& c : words[i]) {
                tempMap[c]++;
            }

            // Perform set intersection to find common characters
            std::set<std::pair<char, int>> intersectionSet;
            for (const auto& pair : commonMap) {
                if (tempMap.find(pair.first) != tempMap.end()) {
                    intersectionSet.insert({pair.first, std::min(pair.second, tempMap[pair.first])});
                }
            }

            // Update the commonMap with the intersection set
            commonMap.clear();
            for (const auto& pair : intersectionSet) {
                commonMap[pair.first] = pair.second;
            }
        }

        // Convert the common characters and frequencies to a vector of strings
        std::vector<std::string> result;
        for (const auto& pair : commonMap) {
            for (int j = 0; j < pair.second; j++) {
                result.push_back(std::string(1, pair.first));
            }
        }

        return result;
    }
};