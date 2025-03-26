/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isCompleteTree = function(root) {
    if (!root) return true;

    const queue = [root];
    let nullFound = false;

    while (queue.length) {
        const node = queue.shift();
        if (node == null){
            nullFound = true;
        } else {
            if (nullFound) {
                return false;
            }
            queue.push(node.left);
            queue.push(node.right);
        }
    }
    return true;
};