# Challenge #38 - Beginner/Intermediate
# Extract unique domains from a list of emails
# Objective: Practice string parsing, validation, and preserving insertion order.

"""
Extract unique domains from a list of emails.
Ignores case, skips invalid emails, and preserves insertion order.
Useful for email processing and backend data cleanup.
"""

def extract_domains(emails):
    """
    Extract unique domains from a list of emails (case-insensitive, ordered).
    """
    # track seen domains to avoid duplicates while preserving output order
    seen = set()
    result = []   # store domains in the order they appear

    for email in emails:
        # normalize email for consistent comparison
        email = email.lower()

        # skip entries that don't have a valid '@' separator
        if "@" not in email:
            continue

        # split at the first '@' and take everything after it as the domain
        domain = email.split("@", 1)[1]

        # add domain only if it hasn't been seen before
        if domain not in seen:
            seen.add(domain)        # mark domain as seen
            result.append(domain)   # append domain to output list

    # return unique domains in original order
    return result


# Example
if __name__ == "__main__":
    sample = [
        "User@Gmail.com",
        "admin@yahoo.com",
        "test@gmail.com",
        "invalid-email",
        "hello@Outlook.com"
    ]
    print(extract_domains(sample))
