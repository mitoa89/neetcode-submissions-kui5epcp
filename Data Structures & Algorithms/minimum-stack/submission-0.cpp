class MinStack {
public:

    std::stack<int> _stack;
    std::map<int, int> _sorted;
    MinStack() {
    }
    
    void push(int val) {
        _stack.push(val);
        _sorted[val] += 1;
    }
    
    void pop() {
        int val = top();
        _stack.pop();
        _sorted[val] -= 1;
        if(_sorted[val] == 0)
            _sorted.erase(val);
    }
    
    int top() {
        return _stack.top();
    }
    
    int getMin() {
        return (_sorted.begin()->first);
    }
};
