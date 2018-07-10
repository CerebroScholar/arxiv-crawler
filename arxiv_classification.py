from typing import NewType


Classification = NewType('Classification', str)

arxiv_classification = {
    'computer_science': Classification('cs'),
    'statistics': Classification('stat')
}
