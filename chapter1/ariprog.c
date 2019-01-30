/*
ID: fuwen.t1
PROB: ariprog
LANG: C++
*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct
{
	int start;
	int step;
}Pro;

static int cmp (const void *sp1, const void *sp2)
{
	const Pro *p1 = (Pro *)sp1;
	const Pro *p2 = (Pro *)sp2;
	if (p1 -> step != p2 -> step)
		return p1 -> step - p2 -> step;
	else
		return p1 -> start - p2 -> start;
}

void sort (Pro *pro, int n, int (*cmp)(const void *, const void *))
{
	Pro tmp;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n - 1; j++)
			if (cmp (&pro[j], &pro[j+1]) > 0)
			{
				tmp = pro[j];
				pro[j] = pro[j+1];
				pro[j+1] = tmp;
			}
}

int main ()
{
	Pro pro[10001];
	int max, n, m, step, count, p, q, k, bisquare[125001];
	FILE *fin = fopen ("ariprog.in", "r");
	FILE *fout = fopen ("ariprog.out", "w");

	fscanf (fin, "%d%d", &n, &m);
	max = 2 * m * m;
	count = step = 1;
	q = p = 0;
	k = 0;

	memset (bisquare, 0, max * sizeof (int));
	memset (pro, 0, 10001 * sizeof (Pro));
	for (int i = 0; i <= m; i++)
		for (int j = i; j <= m; j++)
			bisquare[i * i + j * j] = 1;
	while (p <= max)
	{
		if (bisquare[p])
		{
			for (step = 1; p + (n - 1) * step <= max; step++)
			{
				q = p + step;
				while (q <= max && bisquare[q])
				{
					count++;
					q += step;
					if (count > n)
						break;
				}
				if (count >= n)
				{
					pro[k].start = p;
					pro[k].step = step;
					k++;
				}
				count = 1;
			}
		}
		p++;
	}
	sort (pro, k, cmp);
	if (k == 0)
		fprintf (fout, "NONE\n");
	for (int i = 0; i < k; i++)
		fprintf (fout, "%d %d\n", pro[i].start, pro[i].step);
	return 0;
}


