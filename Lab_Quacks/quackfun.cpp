/**
 * @file quackfun.cpp
 * This is where you will implement the required functions for the
 *  stacks and queues portion of the lab.
 */

namespace QuackFun {

/**
 * Sums items in a stack.
 * @param s A stack holding values to sum.
 * @return The sum of all the elements in the stack, leaving the original
 *  stack in the same state (unchanged).
 *
 * @note You may modify the stack as long as you restore it to its original
 *  values.
 * @note You may use only two local variables of type T in your function.
 *  Note that this function is templatized on the stack's type, so stacks of
 *  objects overloading the + operator can be summed.
 * @note We are using the Standard Template Library (STL) stack in this
 *  problem. Its pop function works a bit differently from the stack we
 *  built. Try searching for "stl stack" to learn how to use it.
 * @hint Think recursively!
 */
template <typename T>
T sum(stack<T>& s)
{
   if(s.empty()) {

     return  0;
   }

   T temp=s.top();
     s.pop();

    T summing=0;
/*summing+=temp;*/
summing=summing+temp+sum(s);
s.push(temp);

return summing;









    // Your code here
   // stub return value (0 for primitive types). Change this!
                // Note: T() is the default value for objects, and 0 for
                // primitive types
}

/**
 * Checks whether the given string (stored in a queue) has balanced brackets.
 * A string will consist of
 * square bracket characters, [, ], and other characters. This function will return
 * true if and only if the square bracket characters in the given
 * string are balanced. For this to be true,
 * all brackets must be matched up correctly, with no extra, hanging, or unmatched
 * brackets. For example, the string "[hello][]" is balanced, "[[][[]a]]" is balanced,
 * "[]]" is unbalanced, "][" is unbalanced, and "))))[cs225]" is balanced.
 *
 * You are allowed only the use of one stack in this function, and no other local variables.
 *
 * @param input The queue representation of a string to check for balanced brackets in
 * @return Whether the input string had balanced brackets
 */
bool isBalanced(queue<char> input)
{


    stack<char> stacks;

    int i=0;
    int k=input.size();
    while(i<k) {

      if(input.front()!='[' && input.front()!= ']') {

        input.pop();
      }



      else  if(input.front()=='['){

        stacks.push('[');
	input.pop();
        if(input.empty()) {
	  return false;
       }

      }
      else if(input.front()==']'){
	if(stacks.empty()) {
	  return false;
	      }
	   stacks.pop();
     input.pop();
	  continue;
      }
      i++;
    }

    if(stacks.empty()) {
      return true;
    } else {
      return false;
    }


}

/**
 * Reverses even sized blocks of items in the queue. Blocks start at sizeqq
 * one and increase for each subsequent block.
 * @param q A queue of items to be scrambled
 *
 * @note Any "leftover" numbers should be handled as if their block was
 *  complete.
 * @note We are using the Standard Template Library (STL) queue in this
 *  problem. Its pop function works a bit differently from the stack we
 *  built. Try searching for "stl stack" to learn how to use it.
 * @hint You'll want to make a local stack variable.
 */
template <typename T>
void scramble(queue<T>& q)
{

queue<T> q2;
stack<T> s;
int count=0;
int k=q.size();
for(int i=0;i<k;i+=count) {
    if(q2.empty()) {
           if(!q.empty()) {
            q2.push(q.front());
             q.pop();}
            count++;
        }

if(count%2==1) {
for(int j=0;j<count+1 && j< k-i;j++)
{
// 2 times //4 times


if(!q.empty()) {
T temp1=q.front();

q.pop();
s.push(temp1);
} }



for(int j=0;j<count+1 && j<k-i;j++) {
// 2 times // 4 times

if(!s.empty()) {
T temp2=s.top();

s.pop();
q2.push(temp2); }
}count++; }

if(count%2!=1) {
// 3 times //5 times
for(int j=0;j<count+1 && j<k-i;j++) {

if(!q.empty()) {
T temp3=q.front();
q.pop();
q2.push(temp3); }}
count++;}
}

q=q2;


}
    // optional: queue<T> q2;

    // Your code here


/**
 * @return true if the parameter stack and queue contain only elements of
 *  exactly the same values in exactly the same order; false, otherwise.
 *
 * @note You may assume the stack and queue contain the same number of items!
 * @note The back of the queue corresponds to the top of the stack!
 * @note There are restrictions for writing this function.
 * - Your function may not use any loops
 * - In your function you may only declare ONE local boolean variable to use in
 *   your return statement, and you may only declare TWO local variables of
 *   parametrized type T to use however you wish.
 * - No other local variables can be used.
 * - After execution of verifySame, the stack and queue must be unchanged. Be
 *   sure to comment your code VERY well.
 */
template <typename T>
bool verifySame(stack<T>& s, queue<T>& q)
{
   //bool retval = true; // optional
    // T temp1; // rename me
    // T temp2; // rename ??

    // Your code here
if(s.empty()){
return true;
} else{
T h = s.top();
s.pop();

bool retval = verifySame(s,q);

T am = q.front();

if((h==am) && retval==true){
retval = true;

}else{
retval=false;
}

s.push(h);
s.push(am);
q.pop();
return retval;
} }
}
