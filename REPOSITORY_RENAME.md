# Repository Renaming Guide

## Overview

This document provides instructions for completing the repository rename from `resume-intelligence` to `ResumeMatch`.

## What Has Been Updated

The following documentation files have been created/updated to reflect the new name **ResumeMatch**:

- ✅ `README.md` - Updated with new repository name and links
- ✅ `CONTRIBUTING.md` - Contributing guidelines using the new name
- ✅ `REPOSITORY_RENAME.md` - This guide

## GitHub Repository Rename Steps

To complete the repository rename on GitHub, follow these steps:

### 1. Rename the Repository on GitHub

1. Go to your repository: https://github.com/anshuman-nanda/resume-intelligence
2. Click on **Settings** (requires admin access)
3. Under the **General** section, find the **Repository name** field
4. Change `resume-intelligence` to `ResumeMatch`
5. Click **Rename**

⚠️ **Important**: GitHub will automatically set up redirects from the old URL to the new one, so existing links will continue to work.

### 2. Update Local Repository (For All Contributors)

After renaming on GitHub, update your local repository:

```bash
# Navigate to your local repository
cd resume-intelligence

# Update the remote URL
git remote set-url origin https://github.com/anshuman-nanda/ResumeMatch.git

# Verify the change
git remote -v

# Optional: Rename your local directory to match
cd ..
mv resume-intelligence ResumeMatch
cd ResumeMatch
```

### 3. Update External References (If Any)

Check and update references in:

- **Package managers** (PyPI, npm, etc.) - Update package names if published
- **Documentation sites** - Update any external documentation
- **CI/CD configurations** - Update GitHub Actions, Travis CI, etc.
- **Badges** - Update any shields.io or similar badges
- **Social media** - Update any social media profiles or posts
- **Blog posts** - Update any blog posts or articles mentioning the old name

### 4. Communicate the Change

Notify users and contributors about the rename:

1. Create a GitHub Release announcing the rename
2. Update your profile or organization README
3. Post an issue or discussion in the repository
4. Update any relevant community channels

### 5. Post-Rename Checklist

- [ ] Repository renamed on GitHub
- [ ] Local repositories updated by all contributors
- [ ] CI/CD pipelines tested and working
- [ ] External documentation updated
- [ ] Package registries updated (if applicable)
- [ ] Social media and external links updated
- [ ] Contributors notified
- [ ] Old URL redirect verified working

## Benefits of the New Name

**ResumeMatch** offers several advantages over `resume-intelligence`:

1. **More Memorable**: Shorter and easier to remember
2. **Clearer Purpose**: Immediately conveys the matching/analysis functionality
3. **Industry Alignment**: Matches the naming patterns of successful similar tools (Resume-Matcher, CVAnalyzer, HireBoost)
4. **Modern**: Uses PascalCase, which is contemporary and professional
5. **Brandable**: Easier to brand and market

## Backward Compatibility

GitHub automatically maintains redirects from the old repository URL to the new one:

- Old URL: `https://github.com/anshuman-nanda/resume-intelligence`
- New URL: `https://github.com/anshuman-nanda/ResumeMatch`

Both URLs will work, ensuring that:
- Existing clones continue to work
- Old bookmarks and links remain functional
- External references automatically redirect

## Questions or Issues?

If you encounter any issues during the rename process, please:

1. Check GitHub's official documentation on [renaming repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/renaming-a-repository)
2. Open an issue in the repository
3. Contact the maintainer

---

**Last Updated**: December 27, 2024  
**Status**: Ready for GitHub rename
