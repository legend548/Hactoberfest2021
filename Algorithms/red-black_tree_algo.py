RB-INSERT(T, k)
     BST-INSERT(T, k) //normal BST insertion
     while k.parent.color == RED
         if k.parent == k.parent.parent.right
            u = k.parent.parent.left //uncle
             if u.color == RED // case 3.1
                u.color = BLACK
                k.parent.color = BLACK
                k.parent.parent.color = RED
                k = k.parent.parent
             else if k == k.parent.left // case 3.3.1 and 3.3.2
                    k = k.parent
                    LEFT-ROTATE(T, k)
                k.parent.color = BLACK
                k.parent.parent.color = RED
                RIGHT-ROTATE(T, k.parent.parent)
        else (same as then clause with “left” and “right” exchanged)
     T.root.color = BLACK
