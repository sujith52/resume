def rank_candidates(candidates):
    """
    Sort candidates by score in descending order.
    """

    return sorted(
        candidates,
        key=lambda candidate: candidate["score"],
        reverse=True
    )