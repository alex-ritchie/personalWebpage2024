# data/publications.py

PUBLICATIONS = [
    {
        'title': 'Online Platforms and the Fair Exposure Problem under Homophily',
        'venue': 'AAAI 2023',
        'conference': 'The Thirty-Seventh AAAI Conference on Artificial Intelligence',
        'authors': 'Jakob Schoeffer*, Alexander Ritchie*, Keziah Naggita*, Faidra Monachou*, Jessie Finocchiaro*, Marc Juarez',
        'year': 2023,
        'abstract': 'We introduce the fair exposure problem in online platforms, studying how to balance content exposure between different user groups while maximizing engagement. Our work develops a theoretical framework for analyzing content propagation under homophily, proving that fairness-agnostic approaches lead to group-homogeneous targeting. We demonstrate that even with fairness constraints, optimal solutions may still target one group with limited content diversity.',
        'paper_url': 'static/content/papers/fair-exposure-homophily-aaai23.pdf',
        'code_url': 'https://github.com/jfinocchiaro/fair-exposure'
    },
    {
        'title': 'Consistent Estimation of Identifiable Nonparametric Mixture Models from Grouped Observations',
        'venue': 'NeurIPS 2020',
        'conference': 'The 34th Conference on Neural Information Processing Systems',
        'year': 2020,
        'authors': 'Alexander Ritchie, Robert A. Vandermeulen, Clayton Scott',
        'abstract': 'Recent research has established sufficient conditions for finite mixture models to be identifiable from grouped observations, even allowing substantial overlap among components. This paper proposes an algorithm for consistently estimating any identifiable mixture model from grouped observations. The approach is based on an oracle inequality for weighted kernel density estimators and shows that consistent estimation of grouped distributions leads to consistent estimation of mixture components. The paper provides a practical algorithm for paired observations and demonstrates its effectiveness in outperforming existing methods, especially with significantly overlapping components.',
        'paper_url': 'static/content/papers/NeurIPS-2020-consistent-estimation-of-identifiable-nonparametric-mixture-models-from-grouped-observations-Paper.pdf',
        'code_url': 'https://github.com/alex-ritchie/NDIGO'
    },
    {
        'title': 'A Proposal for Supervised Density Estimation',
        'venue': 'NeurIPS 2020',
        'conference': 'Pre-registration workshop at the 34th Conference on Neural Information Processing Systems',
        'year': 2020,
        'authors': 'Robert A. Vandermeulen, René Saitenmacher, Alexander Ritchie',
        'abstract': 'This paper introduces supervised density estimation, where samples from a target density are supplemented by auxiliary samples from a contrasting density that the model should avoid. It presents two methods to incorporate contrastive samples in density estimation and demonstrates improvement for tasks such as anomaly detection. The proposed approaches are theoretically grounded, computationally efficient, and adaptable to models from Gaussian mixtures to variational autoencoders.',
        'paper_url': 'static/content/papers/sde-pr.pdf',
        'code_url': ''
    },
        {
        'title': 'Supervised PCA: A Multiobjective Approach',
        'venue': 'arXiv',
        'conference': 'arXiv Preprint',
        'year': 2020,
        'authors': 'Alexander Ritchie, Laura Balzano, Daniel Kessler, Chandra S. Sripada, Clayton Scott',
        'abstract': 'This paper introduces a multiobjective approach to supervised PCA (SPCA) that jointly optimizes prediction accuracy and variance explained by the learned representation. It supports arbitrary loss functions and outperforms existing SPCA methods in both explained variance and predictive power, enabling extensions such as generalized linear models and kernel-based methods.',
        'paper_url': 'static/content/papers/lspca-arxiv.pdf',
        'code_url': 'https://github.com/alex-ritchie/LSPCA'
    },
    {
        'title': 'Controlled Sequential Shape Changing Components by 3D Printing of Shape Memory Polymer Multimaterials',
        'venue': 'IUTAM Symposium',
        'conference': 'IUTAM Symposium on Mechanics of Soft Active Materials, Procedia IUTAM',
        'year': 2015,
        'authors': 'Kai Yu, Alexander Ritchie, Yiqi Mao, Martin L. Dunn, H. Jerry Qi',
        'abstract': 'This study explores the use of 3D printing to create functionally graded shape memory polymers (SMPs) with controlled shape recovery. By tailoring the thermal properties across different sections, these SMPs exhibit programmable shape changes in response to heat, achieving applications in biomedical and aerospace fields. The approach demonstrates enhanced control of recovery sequence via multimaterial SMP design.',
        'paper_url': 'static/content/papers/3DPrintingShapeMemoryPolymerMultimaterials.pdf',
        'code_url': ''
    },
    {
        'title': 'Supervised Principal Component Analysis Via Manifold Optimization',
        'venue': 'DSW 2019',
        'conference': 'IEEE Data Science Workshop',
        'year': 2019,
        'authors': 'Alexander Ritchie, Clayton Scott, Laura Balzano, Daniel Kessler, Chandra S. Sripada',
        'abstract': 'This work presents a novel supervised principal component analysis (SPCA) approach using manifold optimization. The method simultaneously tackles prediction and dimensionality reduction to enhance interpretability and accuracy. This framework is flexible for both regression and classification, outperforming existing SPCA approaches by explaining high variation and improving predictive performance.',
        'paper_url': 'static/content/papers/lspcaDSW19.pdf',
        'code_url': ''  
    },
    


]