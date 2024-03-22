/*
You start with an initial power of power, an initial score of 0, and a bag of tokens given as an integer array tokens, where each tokens[i] donates the value of tokeni.

Your goal is to maximize the total score by strategically playing these tokens. In one move, you can play an unplayed token in one of the two ways (but not both for the same token):

    Face-up: If your current power is at least tokens[i], you may play tokeni, losing tokens[i] power and gaining 1 score.
    Face-down: If your current score is at least 1, you may play tokeni, gaining tokens[i] power and losing 1 score.

Return the maximum possible score you can achieve after playing any number of tokens.
*/
public class Solution {
    public int BagOfTokensScore(int[] tokens, int power) {
        if(tokens.Length == 0){
            return 0;
        }
        // maximise face-up plays, face-down the largest tokens
        int score = 0;
        Array.Sort(tokens);
        //Console.Write(tokens[0] + "," + tokens[tokens.Length-1]);
        int l = 0;
        int r = tokens.Length-1;
        while(l < r){
            if(power >= tokens[l]){
                //Console.Write($"token:{tokens[l]} up:{true}\n");
                power -= tokens[l++];
                score++;
            }else if(score > 0){
                //Console.Write($"token:{tokens[r]} up:{false}\n");
                score--;
                power += tokens[r--];
            }else{
                break;
            }
            //Console.Write($"score:{score}, power:{power}, l:{l}, r:{r}\n");
        }
        // check if the last token can be placed up
        if(power >= tokens[r]){
            //Console.Write($"token:{tokens[r]} up:{true}\n");
            power -= tokens[r--];
            score++;
        }
        return score;
    }
}