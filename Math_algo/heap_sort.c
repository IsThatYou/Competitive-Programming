void siftDown(struct ListNode ** heap, int size,int index)
{
    
    int left = 2 * index +1;
    int right = 2*index +2;
    //printf("left%d\n",left);
    if (left >=size) return;
    int min;
    if (right>=size)
        min = left;
    else
    {
        min = heap[left]->val<heap[right]->val?left:right;
    }
    //printf("min:%d\n",min);
    if (heap[min]->val < heap[index]->val)
    {
        //swap these two, and recurse
        struct ListNode * temp = heap[min];
        heap[min] = heap[index];
        heap[index] = temp;
        siftDown(heap,size,min);
    }
        // else
        // {
        //     return;
        // }
    
}
void BuildHeap(struct ListNode ** heap, int size)
{
    int ruasize = (size-1)/2;
    for (int i = ruasize;i>=0;--i)
    {
        siftDown(heap,size,i);
        //printf("fen ge\n");
    }
    // for (int i = 0;i<size;++i)
    // {
    //     printf("%d ",heap[i]->val);
    // }
    // printf("rua %d\n",size);
}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    struct ListNode * ans = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode * cur = ans;
    struct ListNode * int_max = (struct ListNode *) malloc(sizeof(struct ListNode));
    int_max->val = INT_MAX;
    int_max->next = NULL;
    if (listsSize==0)
    {
        return NULL;
    }
    for (int i = 0;i<listsSize;++i)
    {
        if (lists[i] ==NULL)
            lists[i] = int_max;
    }
    BuildHeap(lists,listsSize);

    return ans;
}