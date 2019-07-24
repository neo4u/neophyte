Node *merging(Node *a, Node *b)
{
    Node *c;
    if (b == NULL)
        return a;
    if (a == NULL)
    {
        c = new Node();
        c->data = b->data;
        c->next = NULL;
        c->bottom = merging(a, b->bottom);
        return c;
    }
    if (a->data <= b->data)
    {
        c = new Node();
        c->data = a->data;
        c->next = NULL;
        c->bottom = merging(a->bottom, b);
        return c;
    }
    else
    {
        c = new Node();
        c->data = b->data;
        c->next = NULL;
        c->bottom = merging(a, b->bottom);
        return c;
    }
}

Node *flatten(Node *root)
{
    if (root == NULL)
        return NULL;
    Node *t = flatten(root->next);
    Node *f = merging(root, t);
    return f;
}
