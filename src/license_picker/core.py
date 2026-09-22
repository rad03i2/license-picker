from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Iterable


@dataclass(frozen=True)
class License:
    id: str
    name: str
    permissions: tuple[str, ...]
    conditions: tuple[str, ...]
    limitations: tuple[str, ...]
    commercial: bool
    patent_grant: bool
    copyleft: str
    notice_required: bool

    def to_dict(self) -> dict:
        return asdict(self)


LICENSES: tuple[License, ...] = (
    License("mit", "MIT License", ("commercial use", "modification", "distribution", "private use"), ("include copyright and license notice",), ("liability", "warranty"), True, False, "none", True),
    License("apache-2.0", "Apache License 2.0", ("commercial use", "modification", "distribution", "private use", "patent use"), ("include license", "state significant changes", "preserve notices"), ("liability", "warranty", "trademark use"), True, True, "none", True),
    License("gpl-3.0", "GNU GPL v3.0", ("commercial use", "modification", "distribution", "private use", "patent use"), ("disclose source when distributing", "license derivatives under GPL-3.0", "include license", "state changes"), ("liability", "warranty"), True, True, "strong", True),
    License("lgpl-3.0", "GNU LGPL v3.0", ("commercial use", "modification", "distribution", "private use", "patent use"), ("disclose library source when distributing modifications", "license library modifications under LGPL-3.0", "include license", "state changes"), ("liability", "warranty"), True, True, "library", True),
    License("mpl-2.0", "Mozilla Public License 2.0", ("commercial use", "modification", "distribution", "private use", "patent use"), ("disclose modified MPL-covered files", "keep MPL-covered files under MPL-2.0", "include license"), ("liability", "warranty", "trademark use"), True, True, "file", True),
    License("bsd-3-clause", "BSD 3-Clause License", ("commercial use", "modification", "distribution", "private use"), ("retain copyright, conditions and disclaimer", "do not use contributor names for endorsement"), ("liability", "warranty"), True, False, "none", True),
    License("unlicense", "The Unlicense", ("commercial use", "modification", "distribution", "private use"), (), ("liability", "warranty"), True, False, "none", False),
)


def get_license(identifier: str) -> License:
    key = identifier.strip().lower()
    for item in LICENSES:
        if item.id == key:
            return item
    raise ValueError(f"unknown license: {identifier}")


def recommend(*, patent_grant: bool = False, copyleft: str = "any", notice_required: bool | None = None) -> list[License]:
    allowed = {"any", "none", "file", "library", "strong"}
    if copyleft not in allowed:
        raise ValueError(f"copyleft must be one of: {', '.join(sorted(allowed))}")
    result: Iterable[License] = LICENSES
    if patent_grant:
        result = (x for x in result if x.patent_grant)
    if copyleft != "any":
        result = (x for x in result if x.copyleft == copyleft)
    if notice_required is not None:
        result = (x for x in result if x.notice_required is notice_required)
    return list(result)


def compare(identifiers: Iterable[str]) -> list[License]:
    seen: set[str] = set()
    result: list[License] = []
    for identifier in identifiers:
        item = get_license(identifier)
        if item.id not in seen:
            seen.add(item.id)
            result.append(item)
    if not result:
        raise ValueError("at least one license is required")
    return result
